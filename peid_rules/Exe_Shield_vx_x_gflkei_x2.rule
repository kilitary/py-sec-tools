rule _Exe_Shield_vx_x_gflkei
{
	meta:
		description = "Exe Shield vx_x"
	strings:
		$a = {53E8000000005B8BC32D}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
