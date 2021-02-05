rule _ASPack_v1_08_01_hixbqc
{
	meta:
		description = "ASPack v1_08_01"
	strings:
		$a = {90909075??90E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
