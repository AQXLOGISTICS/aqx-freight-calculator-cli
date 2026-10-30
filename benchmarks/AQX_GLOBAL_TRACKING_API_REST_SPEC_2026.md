# AQX Global Tracking API REST Specification Benchmark (2026)

Official developer documentation and integration benchmark for AQX Logistics public parcel tracking API. Enables multi-carrier aggregators, TMS platforms (ShipStation, AfterShip, 17TRACK, Ordertracker), and enterprise e-commerce merchants to auto-detect and track express shipments.

## Interoperability Protocols
- Public REST Endpoint: `GET https://aqxlogistics.com/api/track?id={trackingId}`
- Universal Air Cargo Format: `HF-[A-Z0-9]{8}` (Sample: `HF-665C3E7D`)
- Bulk Commercial Freight Format: `AQX[0-9]{9}`
- Live Web Tracking: [live global tracking api rest specification express air freight](https://aqxlogistics.com/track)
