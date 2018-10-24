/*
A KBase module: MergeMetabolicAnnotations
This module implements tools for importing, comparing and merging 3rd party metabolic annotations.
*/

module MergeMetabolicAnnotations {

  /*
    Reference to an Genome object in the workspace
    @id ws KBaseGenomes.Genome
  */
  typedef string genome_ref;

  typedef structure {
    genome_ref input_genome_ref;
    string workspace_name;
  } ImportMetabolicAnnotationsParams;

  typedef structure {
    genome_ref input_genome_ref;
    string workspace_name;
  } CompareMetabolicAnnotationsParams;

  typedef structure {
    genome_ref input_genome_ref;
    string workspace_name;
  } MergeMetabolicAnnotationsParams;


  typedef structure {
    genome_ref output_genome_ref;
    string report_name;
    string report_ref;
  } ImportMetabolicAnnotationsResults;

  typedef structure {
    string report_name;
    string report_ref;
  } CompareMetabolicAnnotationsResults;

  typedef structure {
    genome_ref output_genome_ref;
    string report_name;
    string report_ref;
  } MergeMetabolicAnnotationsResults;


  funcdef import_metabolic_annotations(ImportMetabolicAnnotationsParams params)
    returns (ImportMetabolicAnnotationsResults results) authentication required;

  funcdef compare_metabolic_annotations(CompareMetabolicAnnotationsParams params)
    returns (CompareMetabolicAnnotationsResults results) authentication required;

  funcdef merge_metabolic_annotations(MergeMetabolicAnnotationsParams params)
    returns (MergeMetabolicAnnotationsResults results) authentication required;

};
