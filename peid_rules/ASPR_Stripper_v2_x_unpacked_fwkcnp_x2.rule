rule _ASPR_Stripper_v2_x_unpacked_fwkcnp
{
	meta:
		description = "ASPR Stripper v2_x unpacked"
	strings:
		$a = {BB????????00??????????29????4EE8}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
