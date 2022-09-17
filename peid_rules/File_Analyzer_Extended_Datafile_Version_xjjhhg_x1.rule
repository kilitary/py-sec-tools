rule _File_Analyzer_Extended_Datafile_Version_xjjhhg
{
	meta:
		description = "File Analyzer Extended Datafile Version"
	strings:
		$a = {230345585444????3A03}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
