rule _ASPack_v2_11_yhwmbd
{
	meta:
		description = "ASPack v2_11"
	strings:
		$a = {60E93D040000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
