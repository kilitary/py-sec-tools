rule _AMGC_Archive_tzohpm
{
	meta:
		description = "AMGC Archive"
	strings:
		$a = {AD362200}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
