rule _dePACK__deNULL_djmcru
{
	meta:
		description = "dePACK __ deNULL"
	strings:
		$a = {EB01DD606800??????68??????00E8??000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
