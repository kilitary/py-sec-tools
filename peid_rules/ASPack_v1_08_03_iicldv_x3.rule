rule _ASPack_v1_08_03_iicldv
{
	meta:
		description = "ASPack v1_08_03"
	strings:
		$a = {60E8000000005D81ED0A4A4400BB044A440003DD}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
