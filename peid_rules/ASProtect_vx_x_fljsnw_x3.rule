rule _ASProtect_vx_x_fljsnw
{
	meta:
		description = "ASProtect vx_x"
	strings:
		$a = {906090E8000000005D81EDD1274000B915000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
