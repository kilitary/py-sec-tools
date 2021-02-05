rule _ASPack_v1_08_04_fzoehe
{
	meta:
		description = "ASPack v1_08_04"
	strings:
		$a = {60E841060000EB41}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
