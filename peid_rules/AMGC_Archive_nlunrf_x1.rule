rule _AMGC_Archive_nlunrf
{
	meta:
		description = "AMGC Archive"
	strings:
		$a = {AD362200}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
