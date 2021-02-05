rule _ASPack_v2_1_rxxkks
{
	meta:
		description = "ASPack v2_1"
	strings:
		$a = {60E803000000E9EB045D4555C3E801000000EB5DBBEDFFFFFF03DD81EB}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
