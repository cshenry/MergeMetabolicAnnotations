# -*- coding: utf-8 -*-
#BEGIN_HEADER
#END_HEADER


class MergeMetabolicAnnotations:
    '''
    Module Name:
    MergeMetabolicAnnotations

    Module Description:
    A KBase module: MergeMetabolicAnnotations
This module implements tools for importing, comparing and merging 3rd party metabolic annotations.
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = "https://github.com/jeffkimbrel/MergeMetabolicAnnotations"
    GIT_COMMIT_HASH = "c97c2a861638ba7ee81821112a528020e2ddfd9e"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.version = 1
        self.callback_url = config['SDK_CALLBACK_URL']
        self.token = config['KB_AUTH_TOKEN']
        self.dfu = DataFileUtil(self.callback_url)
        self.uploader_utils = UploaderUtil(config)
        self.ontology_lookup = {
            "ec": "KBaseOntology/ec_ontology",
            "keggko": "KBaseOntology/ko_ontology",
            "keggro": "KBaseOntology/keggro_ontology",
            "metacyc": "KBaseOntology/metacyc_ontology",
            "modelseed": "KBaseOntology/modelseed_ontology"
        }
        #END_CONSTRUCTOR
        pass


    def import_annotations(self, ctx, params):
        """
        :param params: instance of mapping from String to unspecified object
        :returns: instance of type "ReportResults" -> unspecified object
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN import_annotations
        log('--->\nrunning MergeMetabolicAnnotations.import_annotations\n' +
            'params:\n{}'.format(json.dumps(params, indent=1)))

        #self.validate_import_media_from_staging_params(params)

        download_staging_file_params = {
            'staging_file_subdir_path': params.get('annotation_file')
        }
        scratch_file_path = self.dfu.download_staging_file(
                        download_staging_file_params).get('copy_file_path')
        file = {
            'path': scratch_file_path
        }
        
        #Enter python code to parse TSV file with name scratch_file_path
        #LLNL
        
        #Get ontology dictiona object
        if !self.ontology_lookup.get('params.get('ontology')'):
            raise ValueError('params.get('ontology')'+" not found in system!")
        
        get_output = self.dfu.get_objects({
            'object_refs': [self.ontology_lookup.get('params.get('ontology')')]
        })['data'][0]
        ontology_ref = get_output['info'][]+"/"+get_output['info'][]+"/"+get_output['info'][]
        ontology_object = get_output['data']                                                           
        
        #Validate all input ontology terms against ontology dictionary (either filter out bad terms or throw error)
        #LLNL
        
        #Retrieve genome object from workspace
        genomeobj = self.dfu.get_objects({
            'object_refs': [params.get('genome')]
        })['data'][0]['data']
        
        #Validate all input gene IDs against the genes,cds, or mRNA in the genome object
        #LLNL
                                                                                                 
        #Load up ontology events
        new_ontology_event = {
                "id": params.get('name'),
                "method": "MergeMetabolicAnnotations.import_annotations",
                "method_version": self.version,
                "ontology_ref": ontology_ref,
                "timestamp": timestamp,
                "description": params.get('description')
            }
        
        ontology_events = genomeobj.get('ontology_events')
        if ontology_events:        
            ontology_events.append()
        else:
            ontology_events = [new_ontology_event];
            genomeobj['ontology_events'] = ontology_events
                     
        #Load up ontology terms in genomes features
        #LLNL
        
        #Save genome objects back to workspace setting the genome_ref variable to the workspace reference
        #ANL
        
        self.uploader_utils.update_staging_service(params.get('annotation_file'), genome_ref)

        output = {'obj_ref': ref.get('ref')}
        #END import_annotations

        # At some point might do deeper type checking...
        if not isinstance(output, object):
            raise ValueError('Method import_annotations return value ' +
                             'output is not type object as required.')
        # return the results
        return [output]

    def compare_metabolic_annotations(self, ctx, params):
        """
        :param params: instance of mapping from String to unspecified object
        :returns: instance of type "ReportResults" -> unspecified object
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN compare_metabolic_annotations
        #END compare_metabolic_annotations

        # At some point might do deeper type checking...
        if not isinstance(output, object):
            raise ValueError('Method compare_metabolic_annotations return value ' +
                             'output is not type object as required.')
        # return the results
        return [output]

    def merge_metabolic_annotations(self, ctx, params):
        """
        :param params: instance of mapping from String to unspecified object
        :returns: instance of type "ReportResults" -> unspecified object
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN merge_metabolic_annotations
        #END merge_metabolic_annotations

        # At some point might do deeper type checking...
        if not isinstance(output, object):
            raise ValueError('Method merge_metabolic_annotations return value ' +
                             'output is not type object as required.')
        # return the results
        return [output]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
