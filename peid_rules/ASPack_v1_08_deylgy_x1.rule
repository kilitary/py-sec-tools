rule _ASPack_v1_08_deylgy
{
	meta:
		description = "ASPack v1_08"
	strings:
		$a = {60EB035DFFE5E8F8FFFFFF81ED1B6A4400BB106A440003DD2B9D2A}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
