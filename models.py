import datetime
from dataclasses import dataclass
from typing import Optional, List


@dataclass
class Contact:
    Name: Optional[str] = None
    Title: Optional[str] = None


@dataclass
class Location:
    Latitude: Optional[float] = None
    Longitude: Optional[float] = None


@dataclass
class Address:
    Line1: Optional[str] = None
    Line2: Optional[str] = None
    City: Optional[str] = None
    Region: Optional[str] = None
    PostalCode: Optional[str] = None
    Country: Optional[str] = None
    Location: Optional[Location] = None


@dataclass
class Company:
    Id: Optional[str] = None
    ExternalId: Optional[str] = None
    Name: Optional[str] = None
    Contact: Optional[Contact] = None
    Address: Optional[Address] = None
    Phone: Optional[str] = None
    Fax: Optional[str] = None


@dataclass
class Category:
    Id: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None


@dataclass
class OrderLine:
    Product: Optional[str] = None
    ProductName: Optional[str] = None
    PricePerUnit: Optional[int] = None
    Quantity: Optional[int] = None
    Discount: Optional[int] = None


@dataclass
class Order:
    Id: Optional[str] = None
    Company: Optional[str] = None
    Employee: Optional[str] = None
    OrderedAt: Optional[datetime.datetime] = None
    RequiredAt: Optional[datetime.datetime] = None
    ShippedAt: Optional[datetime.datetime] = None
    ShipTo: Optional[Address] = None
    ShipVia: Optional[str] = None
    Freight: Optional[int] = None
    Lines: Optional[List[OrderLine]] = None


@dataclass
class Product:
    Id: Optional[str] = None
    Name: Optional[str] = None
    Supplier: Optional[str] = None
    Category: Optional[str] = None
    QuantityPerUnit: Optional[str] = None
    PricePerUnit: Optional[str] = None
    UnitsInStock: Optional[str] = None
    UnitsInOrder: Optional[str] = None
    Discontinued: Optional[bool] = None
    ReorderLevel: Optional[int] = None


@dataclass
class Employee:
    Id: Optional[str] = None
    LastName: Optional[str] = None
    FirstName: Optional[str] = None
    Title: Optional[str] = None
    Address: Optional[Address] = None
    HiredAt: Optional[datetime.datetime] = None
    Birthday: Optional[datetime.datetime] = None
    HomePhone: Optional[str] = None
    Extension: Optional[str] = None
    ReportsTo: Optional[str] = None
    Notes: Optional[List[str]] = None
    Territories: Optional[List[str]] = None


@dataclass
class Territory:
    Code: Optional[str] = None
    Name: Optional[str] = None
    Area: Optional[str] = None


@dataclass
class Region:
    Id: Optional[str] = None
    Name: Optional[str] = None
    Territories: Optional[List[Territory]] = None


@dataclass
class Shipper:
    Id: Optional[str] = None
    Name: Optional[str] = None
    Phone: Optional[str] = None
