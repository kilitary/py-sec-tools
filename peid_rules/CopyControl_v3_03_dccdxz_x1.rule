rule _CopyControl_v3_03_dccdxz
{
	meta:
		description = "CopyControl v3_03"
	strings:
		$a = {CC9090EB0B0150515253546133612D35CAD10752D1A13C}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
