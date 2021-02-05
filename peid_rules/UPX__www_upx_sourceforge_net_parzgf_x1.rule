rule _UPX__www_upx_sourceforge_net_parzgf
{
	meta:
		description = "UPX __ www_upx_sourceforge_net"
	strings:
		$a = {60BE??????008DBE??????FF}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
