rule _File_Analyzer_Registration_file_v1_1_wguozc
{
	meta:
		description = "File Analyzer Registration file v1_1"
	strings:
		$a = {24464152454724454E433D??26265245473D??26264558503D}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
