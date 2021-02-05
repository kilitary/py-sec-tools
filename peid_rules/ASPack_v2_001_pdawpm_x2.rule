rule _ASPack_v2_001_pdawpm
{
	meta:
		description = "ASPack v2_001"
	strings:
		$a = {60E872050000EB3387DB9000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
