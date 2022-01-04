import logging, re

logging.basicConfig(level=logging.INFO)

#list_update = ['DIAMETER::persist','HTTP::proxy','MR::message','MR::peer','SIP::persist','TCP::congestion','TCP::pacing','ANTIFRAUD::alert_bait_signatures','ANTIFRAUD::alert_device_id','ANTIFRAUD::alert_forbidden_added_element','SSL::nextproto','RADIUS::avp','SDP::field','SSL::forward_proxy','CRYPTO::decrypt','CRYPTO::encrypt','DIAMETER::avp','LSN::persistence','FLOW::priority']

string_irulesupdate = "DIAMETER::persist|HTTP::proxy|MR::message|MR::peer|SIP::persist|TCP::congestion|TCP::pacing|ANTIFRAUD::alert_bait_signatures|ANTIFRAUD::alert_device_id|ANTIFRAUD::alert_forbidden_added_element|SSL::nextproto|RADIUS::avp|SDP::field|SSL::forward_proxy|CRYPTO::decrypt|CRYPTO::encrypt|DIAMETER::avp|LSN::persistence|FLOW::priority"

#pattern_objectltm = re.compile(r'ltm rule (.*) {')
pattern_objectltm = re.compile('{}'.format(string_irulesupdate))

nb_match = 0

with open('bigip_irules.conf', 'r') as bigipconf:
    for line in bigipconf:
        if pattern_objectltm.search(line):
            print(line)
            nb_match += 1

logging.info('Il y a {} commandes ou event mis à jour dans les versions suivantes'.format(nb_match))
