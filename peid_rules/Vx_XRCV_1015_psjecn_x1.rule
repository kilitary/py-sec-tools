rule _Vx_XRCV_1015_psjecn
{
	meta:
		description = "Vx_ XRCV_1015"
	strings:
		$a = {E8????5E83????53511E06B499CD2180FC21??????????33C0508CD8488EC01FA1????8B}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
