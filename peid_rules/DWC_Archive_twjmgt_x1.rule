rule _DWC_Archive_twjmgt
{
	meta:
		description = "DWC Archive"
	strings:
		$a = {445743}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
