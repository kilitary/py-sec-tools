rule _ASPack_v1_08_zyfxfc
{
	meta:
		description = "ASPack v1_08"
	strings:
		$a = {90907501FFE9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
