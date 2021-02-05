rule _ASPack_v1_08_jlqppl
{
	meta:
		description = "ASPack v1_08"
	strings:
		$a = {907501FFE9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
