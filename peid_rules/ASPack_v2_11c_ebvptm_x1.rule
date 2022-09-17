rule _ASPack_v2_11c_ebvptm
{
	meta:
		description = "ASPack v2_11c"
	strings:
		$a = {60E802000000EB095D5581ED39394400C3E959040000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
