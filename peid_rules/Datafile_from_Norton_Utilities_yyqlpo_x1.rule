rule _Datafile_from_Norton_Utilities_yyqlpo
{
	meta:
		description = "Datafile from Norton Utilities"
	strings:
		$a = {504E4349}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
