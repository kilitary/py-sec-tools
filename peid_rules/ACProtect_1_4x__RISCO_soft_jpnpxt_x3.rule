rule _ACProtect_1_4x__RISCO_soft_jpnpxt
{
	meta:
		description = "ACProtect 1_4x __ RISCO soft"
	strings:
		$a = {4753443102001100}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
