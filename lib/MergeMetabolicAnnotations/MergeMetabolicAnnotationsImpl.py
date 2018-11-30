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
