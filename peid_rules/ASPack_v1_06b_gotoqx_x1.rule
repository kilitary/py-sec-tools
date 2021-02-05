rule _ASPack_v1_06b_gotoqx
{
	meta:
		description = "ASPack v1_06b"
	strings:
		$a = {9090907500E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
