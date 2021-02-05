rule _ASPack_v1_07b_ltrfpn
{
	meta:
		description = "ASPack v1_07b"
	strings:
		$a = {60E8000000005D????????????B8????????03C5}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
