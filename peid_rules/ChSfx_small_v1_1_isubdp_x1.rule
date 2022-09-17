rule _ChSfx_small_v1_1_isubdp
{
	meta:
		description = "ChSfx _small_ v1_1"
	strings:
		$a = {BA????E8????8BEC83EC??8CC8BB????B1??D3EB03C38ED805????89}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
