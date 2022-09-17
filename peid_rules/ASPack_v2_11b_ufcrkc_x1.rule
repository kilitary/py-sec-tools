rule _ASPack_v2_11b_ufcrkc
{
	meta:
		description = "ASPack v2_11b"
	strings:
		$a = {60E802000000EB095D5581ED39394400C3E93D040000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
