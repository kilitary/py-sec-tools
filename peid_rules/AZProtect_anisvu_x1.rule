rule _AZProtect_anisvu
{
	meta:
		description = "AZProtect"
	strings:
		$a = {EB70FC608C804D110070258100400D91BB608C804D11007021811D610D810040CE608C804D11007025812581258125812961418131611D610040B730}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
