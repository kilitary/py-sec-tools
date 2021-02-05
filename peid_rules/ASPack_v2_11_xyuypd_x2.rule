rule _ASPack_v2_11_xyuypd
{
	meta:
		description = "ASPack v2_11"
	strings:
		$a = {60E8F9110000C383}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
