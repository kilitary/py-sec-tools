rule _vcasm_1_0__1_1__vcasm_vrgfmh
{
	meta:
		description = "vcasm 1_0 _ 1_1 __ vcasm"
	strings:
		$a = {EB019A60}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
