/*
A KBase module: MergeMetabolicAnnotations
This module implements tools for importing, comparing and merging 3rd party metabolic annotations.
*/

module MergeMetabolicAnnotations {

  funcdef import_annotations(mapping<string,UnspecifiedObject> params)
    returns (ReportResults output) authentication required;

  funcdef compare_metabolic_annotations(mapping<string,UnspecifiedObject> params)
    returns (ReportResults output) authentication required;

  funcdef merge_metabolic_annotations(mapping<string,UnspecifiedObject> params)
    returns (ReportResults output) authentication required;

};
