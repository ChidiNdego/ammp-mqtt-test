import json
import datetime
import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
from argparse import ArgumentParser


def build_argparser():
    """
    Parse command line arguments.
    :return: command line arguments
    """
    parser = ArgumentParser()
    parser.add_argument("-n", "--hostname", type=str,
                        default="mqtt.stage.ammp.io", help="Broker server hostname")
    parser.add_argument("-p", "--port", type=int,
                        default=8883, help="Broker server port")
    parser.add_argument("-t", "--topic", type=str,
                        default="a/b827eb391de9/data", help="Topic to subscribe to")
    parser.add_argument("-u", "--username", required=True, type=str, default=None,
                        help="Username for authentication")
    parser.add_argument("-P", "--password", required=True, type=str, default=None,
                        help="Authentication password")
    parser.add_argument("-caf", "--cafile", type=str, default="ca-stage.crt",
                        help="Path to CA certification file")
    parser.add_argument("-ka", "--keep_alive", type=int, default=60,
                        help="Max elapse time interval")    
    return parser


def print_output_payload(input):
    output = {}
    output['time'] = datetime.datetime.fromtimestamp(input['t'], datetime.timezone.utc).isoformat('T')
    output['data'] = {}
    counter = 0
    for i in input['r']:
        try:
            if (i['_vid'] not in output['data'].keys()):
                output['data'].update({i['_vid']:{}})
            for j in i:
                if (j[0] == '_') or (i[j] is None):
                    pass
                else:
                    output['data'][i['_vid']][j]=i[j]
        except KeyError:
            counter += 1
    print('Number of Vendor ID Unvailable: {}'.format(counter))
    print(20*'---')
    print(output)


def connect_mqtt(args) -> mqtt:

    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to AMMP MQTT Staging Broker!")
            print(20*'---')
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt.Client()
    client.username_pw_set(args.username, args.password)
    client.tls_set(ca_certs=args.cafile)
    client.on_connect = on_connect
    client.connect(args.hostname, args.port)
    
    return client


def subscribe(args, client: mqtt):
    args.t = args.topic
    def on_message(client, userdata, msg):
        print(f"Receiving Payload from `{msg.topic}` topic")
        print(20*'---')

        decoded_message=str(msg.payload.decode("utf-8"))
        msgs=json.loads(decoded_message)
        print_output_payload(msgs)

    client.subscribe(args.topic)
    client.on_message = on_message


def run():
    # Grab command line args
    args = build_argparser().parse_args()

    client = connect_mqtt(args)
    subscribe(args, client)
    client.loop_forever()


if __name__ == '__main__':
    run()