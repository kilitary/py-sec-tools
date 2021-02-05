rule _ASPack_v1_08_bknckg
{
	meta:
		description = "ASPack v1_08"
	strings:
		$a = {9090907501FFE9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
