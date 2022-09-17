rule _ASPack_v2_000_kwwpic
{
	meta:
		description = "ASPack v2_000"
	strings:
		$a = {60E870050000EB4C}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
