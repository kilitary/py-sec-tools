rule _TPACK_v1_7_Archive_wdpayx
{
	meta:
		description = "TPACK v1_7 Archive"
	strings:
		$a = {??54504143??312E37}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
