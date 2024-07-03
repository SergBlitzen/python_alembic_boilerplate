from sqlalchemy.orm import Mapped, mapped_column, declarative_base


Base = declarative_base()


class Example(Base):
    __tablename__ = "example"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        unique=True,
        nullable=False,
        autoincrement=True,
    )
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
