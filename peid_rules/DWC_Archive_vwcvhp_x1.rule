rule _DWC_Archive_vwcvhp
{
	meta:
		description = "DWC Archive"
	strings:
		$a = {445743}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
