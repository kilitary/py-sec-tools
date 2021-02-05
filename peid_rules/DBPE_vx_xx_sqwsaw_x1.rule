rule _DBPE_vx_xx_sqwsaw
{
	meta:
		description = "DBPE vx_xx"
	strings:
		$a = {0305801AB8????8CCA03D08CC981C1????51B9????510606B1??518CD3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
