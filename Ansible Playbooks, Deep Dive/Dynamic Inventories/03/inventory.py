#!/usr/bin/env python3

'''
Dynamic inventory for Ansible in Python
'''

# Use print functionality from Python 3 for compatibility
from __future__ import print_function

import argparse
import logging

# Attempt to import json, if it fails, import simplejson
try:
    import json
except ImportError:
    import simplejson as json

# Inherit from object for Python 2/3 compatibility
class Inventory(object):

    # Constructor
    def __init__(self, include_hostvars_in_list):

        # Configure logger
        self.configure_logger()

        # Capture and store include_hostvars_in_list
        self.include_hostvars_in_list = include_hostvars_in_list

        # Capture the script command line arguments
        parser = argparse.ArgumentParser()
        parser.add_argument('--list', action='store_true',
                            help='list inventory')
        parser.add_argument('--host', action='store',
                            help='show HOST variables')
        self.args = parser.parse_args()

        # If not called with --host or --list, show usage and exit
        if not (self.args.list or self.args.host):
            parser.print_usage()
            raise SystemExit

        # Capture and store the inventory
        self.define_inventory()

        # When called with --list, print the inventory
        if self.args.list:
            self.print_json(self.list())

        # If called with --host, print host information
        elif self.args.host:
            self.print_json(self.host())

    def define_inventory(self):
        self.groups = {
            "centos": {
                "hosts": ["centos1", "centos2", "centos3"],
                "vars": {
                    "ansible_user": 'root'
                }
            },
            "control": {
                "hosts": ["ubuntu-c"],
            },
            "ubuntu": {
                "hosts": ["ubuntu1", "ubuntu2", "ubuntu3"],
                "vars": {
                    "ansible_become": True,
                    "ansible_become_pass": 'password'
                }
            },
            "fake" : {
               "hosts": ['fake1', 'fake2', 'fake3', 'fake4', 'fake5', 'fake6', 'fake7', 'fake8', 'fake9', 'fake10', 'fake11', 'fake12', 'fake13', 'fake14', 'fake15', 'fake16', 'fake17', 'fake18', 'fake19', 'fake20', 'fake21', 'fake22', 'fake23', 'fake24', 'fake25', 'fake26', 'fake27', 'fake28', 'fake29', 'fake30', 'fake31', 'fake32', 'fake33', 'fake34', 'fake35', 'fake36', 'fake37', 'fake38', 'fake39', 'fake40', 'fake41', 'fake42', 'fake43', 'fake44', 'fake45', 'fake46', 'fake47', 'fake48', 'fake49', 'fake50', 'fake51', 'fake52', 'fake53', 'fake54', 'fake55', 'fake56', 'fake57', 'fake58', 'fake59', 'fake60', 'fake61', 'fake62', 'fake63', 'fake64', 'fake65', 'fake66', 'fake67', 'fake68', 'fake69', 'fake70', 'fake71', 'fake72', 'fake73', 'fake74', 'fake75', 'fake76', 'fake77', 'fake78', 'fake79', 'fake80', 'fake81', 'fake82', 'fake83', 'fake84', 'fake85', 'fake86', 'fake87', 'fake88', 'fake89', 'fake90', 'fake91', 'fake92', 'fake93', 'fake94', 'fake95', 'fake96', 'fake97', 'fake98', 'fake99', 'fake100', 'fake101', 'fake102', 'fake103', 'fake104', 'fake105', 'fake106', 'fake107', 'fake108', 'fake109', 'fake110', 'fake111', 'fake112', 'fake113', 'fake114', 'fake115', 'fake116', 'fake117', 'fake118', 'fake119', 'fake120', 'fake121', 'fake122', 'fake123', 'fake124', 'fake125', 'fake126', 'fake127', 'fake128', 'fake129', 'fake130', 'fake131', 'fake132', 'fake133', 'fake134', 'fake135', 'fake136', 'fake137', 'fake138', 'fake139', 'fake140', 'fake141', 'fake142', 'fake143', 'fake144', 'fake145', 'fake146', 'fake147', 'fake148', 'fake149', 'fake150', 'fake151', 'fake152', 'fake153', 'fake154', 'fake155', 'fake156', 'fake157', 'fake158', 'fake159', 'fake160', 'fake161', 'fake162', 'fake163', 'fake164', 'fake165', 'fake166', 'fake167', 'fake168', 'fake169', 'fake170', 'fake171', 'fake172', 'fake173', 'fake174', 'fake175', 'fake176', 'fake177', 'fake178', 'fake179', 'fake180', 'fake181', 'fake182', 'fake183', 'fake184', 'fake185', 'fake186', 'fake187', 'fake188', 'fake189', 'fake190', 'fake191', 'fake192', 'fake193', 'fake194', 'fake195', 'fake196', 'fake197', 'fake198', 'fake199', 'fake200', 'fake201', 'fake202', 'fake203', 'fake204', 'fake205', 'fake206', 'fake207', 'fake208', 'fake209', 'fake210', 'fake211', 'fake212', 'fake213', 'fake214', 'fake215', 'fake216', 'fake217', 'fake218', 'fake219', 'fake220', 'fake221', 'fake222', 'fake223', 'fake224', 'fake225', 'fake226', 'fake227', 'fake228', 'fake229', 'fake230', 'fake231', 'fake232', 'fake233', 'fake234', 'fake235', 'fake236', 'fake237', 'fake238', 'fake239', 'fake240', 'fake241', 'fake242', 'fake243', 'fake244', 'fake245', 'fake246', 'fake247', 'fake248', 'fake249', 'fake250', 'fake251', 'fake252', 'fake253', 'fake254', 'fake255', 'fake256', 'fake257', 'fake258', 'fake259', 'fake260', 'fake261', 'fake262', 'fake263', 'fake264', 'fake265', 'fake266', 'fake267', 'fake268', 'fake269', 'fake270', 'fake271', 'fake272', 'fake273', 'fake274', 'fake275', 'fake276', 'fake277', 'fake278', 'fake279', 'fake280', 'fake281', 'fake282', 'fake283', 'fake284', 'fake285', 'fake286', 'fake287', 'fake288', 'fake289', 'fake290', 'fake291', 'fake292', 'fake293', 'fake294', 'fake295', 'fake296', 'fake297', 'fake298', 'fake299', 'fake300', 'fake301', 'fake302', 'fake303', 'fake304', 'fake305', 'fake306', 'fake307', 'fake308', 'fake309', 'fake310', 'fake311', 'fake312', 'fake313', 'fake314', 'fake315', 'fake316', 'fake317', 'fake318', 'fake319', 'fake320', 'fake321', 'fake322', 'fake323', 'fake324', 'fake325', 'fake326', 'fake327', 'fake328', 'fake329', 'fake330', 'fake331', 'fake332', 'fake333', 'fake334', 'fake335', 'fake336', 'fake337', 'fake338', 'fake339', 'fake340', 'fake341', 'fake342', 'fake343', 'fake344', 'fake345', 'fake346', 'fake347', 'fake348', 'fake349', 'fake350', 'fake351', 'fake352', 'fake353', 'fake354', 'fake355', 'fake356', 'fake357', 'fake358', 'fake359', 'fake360', 'fake361', 'fake362', 'fake363', 'fake364', 'fake365', 'fake366', 'fake367', 'fake368', 'fake369', 'fake370', 'fake371', 'fake372', 'fake373', 'fake374', 'fake375', 'fake376', 'fake377', 'fake378', 'fake379', 'fake380', 'fake381', 'fake382', 'fake383', 'fake384', 'fake385', 'fake386', 'fake387', 'fake388', 'fake389', 'fake390', 'fake391', 'fake392', 'fake393', 'fake394', 'fake395', 'fake396', 'fake397', 'fake398', 'fake399', 'fake400', 'fake401', 'fake402', 'fake403', 'fake404', 'fake405', 'fake406', 'fake407', 'fake408', 'fake409', 'fake410', 'fake411', 'fake412', 'fake413', 'fake414', 'fake415', 'fake416', 'fake417', 'fake418', 'fake419', 'fake420', 'fake421', 'fake422', 'fake423', 'fake424', 'fake425', 'fake426', 'fake427', 'fake428', 'fake429', 'fake430', 'fake431', 'fake432', 'fake433', 'fake434', 'fake435', 'fake436', 'fake437', 'fake438', 'fake439', 'fake440', 'fake441', 'fake442', 'fake443', 'fake444', 'fake445', 'fake446', 'fake447', 'fake448', 'fake449', 'fake450', 'fake451', 'fake452', 'fake453', 'fake454', 'fake455', 'fake456', 'fake457', 'fake458', 'fake459', 'fake460', 'fake461', 'fake462', 'fake463', 'fake464', 'fake465', 'fake466', 'fake467', 'fake468', 'fake469', 'fake470', 'fake471', 'fake472', 'fake473', 'fake474', 'fake475', 'fake476', 'fake477', 'fake478', 'fake479', 'fake480', 'fake481', 'fake482', 'fake483', 'fake484', 'fake485', 'fake486', 'fake487', 'fake488', 'fake489', 'fake490', 'fake491', 'fake492', 'fake493', 'fake494', 'fake495', 'fake496', 'fake497', 'fake498', 'fake499', 'fake500', 'fake501', 'fake502', 'fake503', 'fake504', 'fake505', 'fake506', 'fake507', 'fake508', 'fake509', 'fake510', 'fake511', 'fake512', 'fake513', 'fake514', 'fake515', 'fake516', 'fake517', 'fake518', 'fake519', 'fake520', 'fake521', 'fake522', 'fake523', 'fake524', 'fake525', 'fake526', 'fake527', 'fake528', 'fake529', 'fake530', 'fake531', 'fake532', 'fake533', 'fake534', 'fake535', 'fake536', 'fake537', 'fake538', 'fake539', 'fake540', 'fake541', 'fake542', 'fake543', 'fake544', 'fake545', 'fake546', 'fake547', 'fake548', 'fake549', 'fake550', 'fake551', 'fake552', 'fake553', 'fake554', 'fake555', 'fake556', 'fake557', 'fake558', 'fake559', 'fake560', 'fake561', 'fake562', 'fake563', 'fake564', 'fake565', 'fake566', 'fake567', 'fake568', 'fake569', 'fake570', 'fake571', 'fake572', 'fake573', 'fake574', 'fake575', 'fake576', 'fake577', 'fake578', 'fake579', 'fake580', 'fake581', 'fake582', 'fake583', 'fake584', 'fake585', 'fake586', 'fake587', 'fake588', 'fake589', 'fake590', 'fake591', 'fake592', 'fake593', 'fake594', 'fake595', 'fake596', 'fake597', 'fake598', 'fake599', 'fake600', 'fake601', 'fake602', 'fake603', 'fake604', 'fake605', 'fake606', 'fake607', 'fake608', 'fake609', 'fake610', 'fake611', 'fake612', 'fake613', 'fake614', 'fake615', 'fake616', 'fake617', 'fake618', 'fake619', 'fake620', 'fake621', 'fake622', 'fake623', 'fake624', 'fake625', 'fake626', 'fake627', 'fake628', 'fake629', 'fake630', 'fake631', 'fake632', 'fake633', 'fake634', 'fake635', 'fake636', 'fake637', 'fake638', 'fake639', 'fake640', 'fake641', 'fake642', 'fake643', 'fake644', 'fake645', 'fake646', 'fake647', 'fake648', 'fake649', 'fake650', 'fake651', 'fake652', 'fake653', 'fake654', 'fake655', 'fake656', 'fake657', 'fake658', 'fake659', 'fake660', 'fake661', 'fake662', 'fake663', 'fake664', 'fake665', 'fake666', 'fake667', 'fake668', 'fake669', 'fake670', 'fake671', 'fake672', 'fake673', 'fake674', 'fake675', 'fake676', 'fake677', 'fake678', 'fake679', 'fake680', 'fake681', 'fake682', 'fake683', 'fake684', 'fake685', 'fake686', 'fake687', 'fake688', 'fake689', 'fake690', 'fake691', 'fake692', 'fake693', 'fake694', 'fake695', 'fake696', 'fake697', 'fake698', 'fake699', 'fake700', 'fake701', 'fake702', 'fake703', 'fake704', 'fake705', 'fake706', 'fake707', 'fake708', 'fake709', 'fake710', 'fake711', 'fake712', 'fake713', 'fake714', 'fake715', 'fake716', 'fake717', 'fake718', 'fake719', 'fake720', 'fake721', 'fake722', 'fake723', 'fake724', 'fake725', 'fake726', 'fake727', 'fake728', 'fake729', 'fake730', 'fake731', 'fake732', 'fake733', 'fake734', 'fake735', 'fake736', 'fake737', 'fake738', 'fake739', 'fake740', 'fake741', 'fake742', 'fake743', 'fake744', 'fake745', 'fake746', 'fake747', 'fake748', 'fake749', 'fake750', 'fake751', 'fake752', 'fake753', 'fake754', 'fake755', 'fake756', 'fake757', 'fake758', 'fake759', 'fake760', 'fake761', 'fake762', 'fake763', 'fake764', 'fake765', 'fake766', 'fake767', 'fake768', 'fake769', 'fake770', 'fake771', 'fake772', 'fake773', 'fake774', 'fake775', 'fake776', 'fake777', 'fake778', 'fake779', 'fake780', 'fake781', 'fake782', 'fake783', 'fake784', 'fake785', 'fake786', 'fake787', 'fake788', 'fake789', 'fake790', 'fake791', 'fake792', 'fake793', 'fake794', 'fake795', 'fake796', 'fake797', 'fake798', 'fake799', 'fake800', 'fake801', 'fake802', 'fake803', 'fake804', 'fake805', 'fake806', 'fake807', 'fake808', 'fake809', 'fake810', 'fake811', 'fake812', 'fake813', 'fake814', 'fake815', 'fake816', 'fake817', 'fake818', 'fake819', 'fake820', 'fake821', 'fake822', 'fake823', 'fake824', 'fake825', 'fake826', 'fake827', 'fake828', 'fake829', 'fake830', 'fake831', 'fake832', 'fake833', 'fake834', 'fake835', 'fake836', 'fake837', 'fake838', 'fake839', 'fake840', 'fake841', 'fake842', 'fake843', 'fake844', 'fake845', 'fake846', 'fake847', 'fake848', 'fake849', 'fake850', 'fake851', 'fake852', 'fake853', 'fake854', 'fake855', 'fake856', 'fake857', 'fake858', 'fake859', 'fake860', 'fake861', 'fake862', 'fake863', 'fake864', 'fake865', 'fake866', 'fake867', 'fake868', 'fake869', 'fake870', 'fake871', 'fake872', 'fake873', 'fake874', 'fake875', 'fake876', 'fake877', 'fake878', 'fake879', 'fake880', 'fake881', 'fake882', 'fake883', 'fake884', 'fake885', 'fake886', 'fake887', 'fake888', 'fake889', 'fake890', 'fake891', 'fake892', 'fake893', 'fake894', 'fake895', 'fake896', 'fake897', 'fake898', 'fake899', 'fake900', 'fake901', 'fake902', 'fake903', 'fake904', 'fake905', 'fake906', 'fake907', 'fake908', 'fake909', 'fake910', 'fake911', 'fake912', 'fake913', 'fake914', 'fake915', 'fake916', 'fake917', 'fake918', 'fake919', 'fake920', 'fake921', 'fake922', 'fake923', 'fake924', 'fake925', 'fake926', 'fake927', 'fake928', 'fake929', 'fake930', 'fake931', 'fake932', 'fake933', 'fake934', 'fake935', 'fake936', 'fake937', 'fake938', 'fake939', 'fake940', 'fake941', 'fake942', 'fake943', 'fake944', 'fake945', 'fake946', 'fake947', 'fake948', 'fake949', 'fake950', 'fake951', 'fake952', 'fake953', 'fake954', 'fake955', 'fake956', 'fake957', 'fake958', 'fake959', 'fake960', 'fake961', 'fake962', 'fake963', 'fake964', 'fake965', 'fake966', 'fake967', 'fake968', 'fake969', 'fake970', 'fake971', 'fake972', 'fake973', 'fake974', 'fake975', 'fake976', 'fake977', 'fake978', 'fake979', 'fake980', 'fake981', 'fake982', 'fake983', 'fake984', 'fake985', 'fake986', 'fake987', 'fake988', 'fake989', 'fake990', 'fake991', 'fake992', 'fake993', 'fake994', 'fake995', 'fake996', 'fake997', 'fake998', 'fake999', 'fake1000']
            },
            "linux": {
                "children": ["centos", "ubuntu"],
            }}

        self.hostvars = {
            'centos1': {
                'ansible_port': 2222
            },
            'ubuntu-c': {
                'ansible_connection': 'local'
            }
        }

    # Pretty print JSON
    def print_json(self, content):
        print(json.dumps(content, indent=4, sort_keys=True))

    # Return inventory dictionary
    def list(self):

        self.logger.info('list executed')

        # If include_hostvars_in_list is True, merge the hostvars
        # as _meta data
        if self.include_hostvars_in_list:
            merged = self.groups
            merged['_meta'] = {}
            merged['_meta']['hostvars'] = self.hostvars
            return merged

        # Otherwise, return the groups without hostvars
        else:
            return self.groups

    # Return host dictionary
    def host(self):

        self.logger.info('host executed for {}'.format(self.args.host))

        # If the requested hosts exists in hostvars, return it
        if self.args.host in self.hostvars:
            return self.hostvars[self.args.host]

        # Otherwise, return an empty list
        else:
            return {}

    # Logger, for debugging as stdout is used by the script
    def configure_logger(self):
        self.logger = logging.getLogger('ansible_dynamic_inventory')
        self.hdlr = logging.FileHandler('/var/tmp/ansible_dynamic_inventory.log')
        self.formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        self.hdlr.setFormatter(self.formatter)
        self.logger.addHandler(self.hdlr) 
        self.logger.setLevel(logging.DEBUG)

# Call the Inventory class constructor (__init__)
# Pass include_hostsvars_in_list as True to include hostvars
# as _meta data in list output
Inventory(include_hostvars_in_list=False)
