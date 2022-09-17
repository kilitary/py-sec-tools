rule _Datafile_from_Norton_Utilities_kueqwl
{
	meta:
		description = "Datafile from Norton Utilities"
	strings:
		$a = {504E4349}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
