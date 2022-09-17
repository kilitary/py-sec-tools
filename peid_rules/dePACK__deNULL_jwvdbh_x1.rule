rule _dePACK__deNULL_jwvdbh
{
	meta:
		description = "dePACK __ deNULL"
	strings:
		$a = {EB01DD606800??????68????0000E8??000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
