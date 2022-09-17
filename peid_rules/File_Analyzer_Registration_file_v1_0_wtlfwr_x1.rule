rule _File_Analyzer_Registration_file_v1_0_wtlfwr
{
	meta:
		description = "File Analyzer Registration file v1_0"
	strings:
		$a = {244641524547244D2D????????31}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
