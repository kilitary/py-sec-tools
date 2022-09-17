rule __NET_executable_vogdlf
{
	meta:
		description = "_NET executable"
	strings:
		$a = {FF2500204000000000000000000000000000000000000000000000000000000000000000000000000000000000000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
