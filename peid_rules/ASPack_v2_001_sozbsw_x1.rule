rule _ASPack_v2_001_sozbsw
{
	meta:
		description = "ASPack v2_001"
	strings:
		$a = {60E872050000EB4C}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
