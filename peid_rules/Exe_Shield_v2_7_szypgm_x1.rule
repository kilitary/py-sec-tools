rule _Exe_Shield_v2_7_szypgm
{
	meta:
		description = "Exe Shield v2_7"
	strings:
		$a = {EB0668F4860600C39C60E8020000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
