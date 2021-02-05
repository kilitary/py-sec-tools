rule _File_Analyzer_Compiled_Datafile_Version_hqnwmn
{
	meta:
		description = "File Analyzer Compiled Datafile Version"
	strings:
		$a = {46696C6520416E616C797A657220436F6D70696C6564204461746166696C652056657273696F6E}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
