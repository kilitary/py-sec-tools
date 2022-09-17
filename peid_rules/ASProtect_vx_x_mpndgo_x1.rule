rule _ASProtect_vx_x_mpndgo
{
	meta:
		description = "ASProtect vx_x"
	strings:
		$a = {9060??????0000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
